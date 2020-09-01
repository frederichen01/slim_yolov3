import torch
from models import *
from thop import profile

model = Darknet('cfg/prune_0.8_keep_0.01_12_shortcut_yolov3-tiny.cfg', (320, 320))
model.fuse()
input = torch.randn(1, 3, 320, 320)
flops, params = profile(model, inputs=(input, ))
print('flops:', flops)
print('params:', params)

