
import torch

model_1 = 'runs/test_lr-5/model.pt'
model_2 = 'pretrained_models/UNETR_model_best_acc.pth'


model_dict_1 = torch.load(model_1)
print(model_dict_1['state_dict'])
# model.load_state_dict(model_dict_1)
print('********************************')
model_dict_2 = torch.load(model_2)
print(model_dict_2)