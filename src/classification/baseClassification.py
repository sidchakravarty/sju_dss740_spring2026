import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import wandb
import graphviz
from sklearn.tree import export_graphviz
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

import warnings
warnings.filterwarnings('ignore')

class BaseClassifier:

    def __init__(self, model_name, model, config = None, useWandB=False, project_name="classification_project"):
        """Initialize the BaseClassifier class.
        
        Inputs:
        1. model_name (str)         : Name of the machine learning model.
        2. model (object)           : The machine learning model object.
        3. hyperparameters (dict)   : Hyperparameters for the machine learning model.
        4. config (dict)            : Additional configuration parameters for the machine learning model.
        5. useWandB (bool)          : Whether to use Weights & Biases for logging (default is False).
        6. project_name (str)       : Name of the Weights & Biases project (default is "classification_project").
        """

        self.model_name = model_name
        self.model = model
        self.config = config if config else {}
        self.useWandB = useWandB

        if self.useWandB:
            wandb.init(project=project_name, config=self.config, name = f"{model_name}_{wandb.util.generate_id()}")
            print(f"Initialized Weights & Biases for {model_name} with run ID: {wandb.run.id}")
            wandb.config.update(self.config)
    
    def train_validation_split(self, X, y, test_size=0.2, random_state=42):
        """Perform a train-validation split on the given data.
        
        Inputs:
        1. X (DataFrame)         : Predictor variables.
        2. y (Series)            : Response variable.
        3. test_size (float)     : Fraction of the data to be used for testing (default is 0.2).
        4. random_state (int)    : Random seed for reproducibility (default is 42).

        Returns:
        1. X_train (DataFrame)  : Training data features.
        2. X_test (DataFrame)   : Validation data features.
        3. y_train (Series)     : Training data labels.
        4. y_test (Series)      : Validation data labels.
        """
        return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
    
    def fit(self, X_train, y_train):
        """Fit the machine learning model using the training data.
        
        Inputs:
        1. X_train (DataFrame) : Training data features.
        2. y_train (Series)   : Training data labels.
        """
        self.model.fit(X_train, y_train)
        return self
    
    def predict(self, X_test):
        """Make predictions using the trained machine learning model.
        
        Inputs:
        1. X_test (DataFrame) : Testing data features.
        
        Returns:
        1. y_pred (Series) : Predictions made by the machine learning model.
        """
        return self.model.predict(X_test)
        
    def predict_proba(self, X_test):
        """Return class probabilities if the model supports it.
        
        Inputs:
        1. X_test (DataFrame) : Testing data features.
        
        Returns:
        1. y_pred_proba (array) : Class probabilities for the testing data.
        
        """
        if hasattr(self.model, "predict_proba"):
            return self.model.predict_proba(X_test)
        else:
            raise AttributeError(f"{self.model_name} does not support probability prediction.")


    def cross_validate(self, X, y, cv=5, scoring='accuracy'):
        """Perform cross-validation and return average score.
        
        Inputs:
        1. X (DataFrame)            : Predictor variables.
        2. y (Series)               : Response variable.
        3. cv (int)                 : Number of folds for cross-validation (default is 5).
        4. scoring (str)            : Evaluation metric for cross-validation (default is 'accuracy').
        
        Returns:
        1. mean_score (float)       : Average score of the cross-validation.
        """
        if self.use_wandb:
            wandb.log({f'cv_{scoring}': scores.mean()})
        scores = cross_val_score(self.model, X, y, cv=cv, scoring=scoring)
        return {'mean_score': scores.mean(), 'all_scores': scores}

    def plot_confusion_matrix(self, X_test, y_test):
        """Plot the confusion matrix for the predictions made by the model.

        Inputs:
        1. X_test (DataFrame)       : Testing data features.
        2. y_test (Series)          : Testing data labels.
        """
        if not hasattr(self.model, 'predict'):
            raise AttributeError(f"{self.model_name} does not have a predict method.")
        y_pred = self.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.title(f'Confusion Matrix - {self.model_name}')
        plt.show()

    def plot_feature_importance(self, feature_names):
        """Plot feature importance for tree-based models.
        
        Inputs:
        1. feature_names (list)         : Names of the features.
        
        """
        if hasattr(self.model, 'feature_importances_'):
            importances = self.model.feature_importances_
            indices = np.argsort(importances)[::-1]
            plt.figure(figsize=(10, 6))
            plt.title(f'Feature Importances - {self.model_name}')
            sns.barplot(x=importances[indices], y=np.array(feature_names)[indices])
            plt.tight_layout()
            plt.show()
        else:
            print(f"{self.model_name} does not support feature importance.")

    
    def evaluate(self, X_test, y_test):
        """Evaluate the performance of the machine learning model using the testing data.
        
        Inputs:
        1. X_test (DataFrame) : Testing data features.
        2. y_test (Series)   : Testing data labels.
        
        Returns:
        1. metrics (dict) : Dictionary containing evaluation metrics such as accuracy, precision, recall, and F1 score.
        """
        y_pred = self.predict(X_test)
        
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average='weighted'),
            'recall': recall_score(y_test, y_pred, average='weighted'),
            'f1_score': f1_score(y_test, y_pred, average='weighted'),
            'classification_report': classification_report(y_test, y_pred),
            'confusion_matrix': confusion_matrix(y_test, y_pred)
        }        

        if self.useWandB:
            wandb.log(metrics)
            wandb.sklearn.plot_confusion_matrix(y_test, y_pred, self.model_name, labels = np.unique(y_test).tolist())
            wandb.sklearn.plot_roc_curve(y_test, y_pred, self.model_name, labels = np.unique(y_test).tolist())
            wandb.sklearn.plot_classifier(self.model, X_test, y_test, self.model_name, labels=np.unique(y_test).tolist())
            print(f"Logged metrics to Weights & Biases for {self.model_name} with run ID: {wandb.run.id}")

        metrics['classification_report'] = metrics['classification_report'].replace('\n', ' ')
        metrics['confusion_matrix'] = metrics['confusion_matrix'].tolist()  # Convert to list for logging
        return metrics
    
    def get_model_name(self):
        """Return the name of the machine learning model."""
        return self.model_name
    
    def get_model(self):
        """Return the machine learning model object."""
        return self.model
        
    def get_hyperparameters(self):
        """Return the hyperparameters of the machine learning model."""
        if hasattr(self.model, 'get_params'):
            return self.model.get_params()
        else:
            return None

    def save_model(self, file_path):
        """Save the trained machine learning model to a file.
        
        Inputs:
        1. file_path (str) : Path to the file where the model will be saved.
        """
        joblib.dump(self.model, file_path)
        print(f"Model saved to {file_path}")
        return self
    
    @staticmethod
    def load_model(self, file_path):
        """Load a trained machine learning model from a file.
        
        Inputs:
        1. file_path (str) : Path to the file where the model is saved.
        
        Returns:
        1. self (BaseClassifier) : The instance of BaseClassifier with the loaded model.
        """
        self.model = joblib.load(file_path)
        print(f"Model loaded from {file_path}")
        return self

    def export_tree_graph(self, feature_names, class_names, file_name="tree"):
        """Export the decision tree as a graphical representation.
        
        Inputs:
        1. feature_names (list)         : Names of the features.
        2. class_names (list)          : Names of the classes.
        3. file_name (str)            : Name of the output file (default is 'tree').

        """
        if isinstance(self.model, DecisionTreeClassifier):
            dot_data = export_graphviz(self.model, out_file=None,
                                    feature_names=feature_names,
                                    class_names=class_names,
                                    filled=True, rounded=True,
                                    special_characters=True)
            graph = graphviz.Source(dot_data)
            graph.render(file_name)
            print(f"Decision tree exported to {file_name}.pdf")
        else:
            print(f"{self.model_name} is not a DecisionTreeClassifier.")

    def finish_run(self):
        """Close the Weights & Biases run."""
        if self.use_wandb:
            wandb.finish()
