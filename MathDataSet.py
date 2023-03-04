import torch.utils.data.dataset as Dataset
import os
import json

class MDataSet(Dataset):
	"""load all data from the toy dataset in Math folder, either from train or test subfolders"""
	def __init__(self, root_dir):
		super(MDataSet, self).__init__()
		self.filelist = []
		for root, dirs, files in os.walk(root_dir):
			for file in files:
			#append the file name to the list
				self.filelist.append(os.path.join(root,file))

	def __getitem__(self, index):
		entry = json.load(open(self.filelist[index]))
		return (entry["problem"], entry["solution"])

	def __len__(self):
		return len(self.filelist)