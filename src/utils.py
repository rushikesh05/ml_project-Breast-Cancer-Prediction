# utils.py

def calculate_accuracy(y_true, y_pred):
    """
    Calculates the accuracy of the predictions.
    
    Args:
        y_true (list or numpy array): The true labels.
        y_pred (list or numpy array): The predicted labels.
        
    Returns:
        float: The accuracy of the predictions.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("The lengths of y_true and y_pred must be equal.")
    
    correct = 0
    total = len(y_true)
    
    for true_label, pred_label in zip(y_true, y_pred):
        if true_label == pred_label:
            correct += 1
    
    accuracy = correct / total
    return accuracy
