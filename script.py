def generate_dataset(dataset, window_size,word_to_index):
  """ Method to generate training dataset for CBOW.
  Arguments
  ---------
  data : String
     Training dataset
  window_size : int
     Size of the context window
  word_to_index : Dictionary
     Dictionary mapping words to index with format {word:index}
  Returns
  -------
  surroundings : N x W Tensor
      Tensor with index of surrounding words, with N being the number of samples and W being the window size
  targets : Tensor
      Tensor with index of target word
  """
  surroundings= []
  targets = []
  # TODO complete the following
  for data in dataset:
    for i in range(window_size,len(data)-window_size):
      surrounding = [i, i+1, i+2, len(data)-window_size-2, len(data)-window_size-1]#get indexes of surrounding words in a list
