import numpy as np
from sklearn.preprocessing import MinMaxScaler

def normalize_features(dataset):
    """
    Normalize the feature vectors in the dataset between -pi and pi.

    Parameters:
    - dataset: 2D array where each row represents a feature vector with the last element being the classification.

    Returns:
    - normalized_dataset: Normalized feature vectors with the classification.
    """
    # Extract feature vectors and classification
    feature_vectors = dataset[:, :-1]  # Exclude the last column (classification)
    classification = dataset[:, -1]  # Extract the classification column

    # Create a MinMaxScaler instance
    scaler = MinMaxScaler(feature_range=(0, np.pi))

    # Fit and transform the feature vectors
    normalized_feature_vectors = scaler.fit_transform(feature_vectors)

    # Concatenate the normalized feature vectors with the classification array
    normalized_dataset = np.hstack((normalized_feature_vectors, classification[:, np.newaxis]))

    return normalized_dataset


np.random.seed(70)

def random_sample(dataset, array_size):
    """
    Randomly sample unique elements from the dataset.

    Parameters:
    - dataset: 2D array where each row represents a feature vector with the last element being the classification.
    - size: Number of samples to be selected.

    Returns:
    - sampled_data: Randomly sampled unique elements from the dataset.
    """
    indices = np.random.choice(dataset.shape[0], size=array_size, replace=False)
    sampled_data = dataset[indices]
    return sampled_data

def sample_pulsars(normalized_dataset, train_size, test_size, num_sets):
    # Separate pulsars and non-pulsars from the dataset
    pulsars = normalized_dataset[normalized_dataset[:, -1] == 1]
    non_pulsars = normalized_dataset[normalized_dataset[:, -1] == 0]
    pulsar_size = int(train_size * 0.5)
    non_pulsar_size = int(train_size * 0.5)
    
    pulsar_size_test = int(test_size * 0.092)#0.908)
    non_pulsar_size_test = int(test_size * 0.908)
    

    # Initialize empty lists for test samples
    test_pulsar_samples = []
    test_non_pulsar_samples = []
    train_pulsar_samples = []
    train_non_pulsar_samples = []
    
    # Loop to create multiple test sets
    for i in range(num_sets):

        # Randomly sample pulsars, non-pulsars, and the test set
        pulsar_samples = random_sample(pulsars, pulsar_size)
        non_pulsar_samples = random_sample(non_pulsars, non_pulsar_size)
        
        test_pulsar_set = random_sample(pulsars, pulsar_size_test)
        test_non_pulsar_set = random_sample(non_pulsars, non_pulsar_size_test)

        # Append to the overall test sets
        test_pulsar_samples.append(test_pulsar_set)
        test_non_pulsar_samples.append(test_non_pulsar_set)
        
        train_pulsar_samples.append(pulsar_samples)
        train_non_pulsar_samples.append(non_pulsar_samples)


    # Convert lists to numpy arrays
    test_pulsar_samples = np.array(test_pulsar_samples)
    test_non_pulsar_samples = np.array(test_non_pulsar_samples)
    
    train_pulsar_samples = np.array(train_pulsar_samples)
    train_non_pulsar_samples = np.array(train_non_pulsar_samples)

    return train_pulsar_samples, train_non_pulsar_samples, test_pulsar_samples, test_non_pulsar_samples





def feature_class_split(data):
    features = data[:, :8]
    classifications = data[:, 8]
    return features,classifications

def normalize():
    dataset = np.genfromtxt('pulsar.csv', delimiter = ',', skip_header=1)
    #feature_vectors,classification = feature_class_split(dataset)
    normalized_dataset = normalize_features(dataset)
    return normalized_dataset
