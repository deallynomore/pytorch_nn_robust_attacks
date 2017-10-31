from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from net_sphere import AngleLinear
import numpy as np
import math


class LeNetpp(nn.Module):
    def __init__(self):
        super().__init__()
        self.stage1 = nn.Sequential(
            nn.Conv2d(1, 32, 5, stride=1, padding=2),
            nn.Conv2d(32, 32, 5, stride=1, padding=2),
            nn.MaxPool2d(2, stride=2, padding=0)
        )
        self.stage2 = nn.Sequential(
            nn.Conv2d(32, 64, 5, stride=1, padding=2),
            nn.Conv2d(64, 64, 5, stride=1, padding=2),
            nn.MaxPool2d(2, stride=2, padding=0)
        )
        self.stage3 = nn.Sequential(
            nn.Conv2d(64, 128, 5, stride=1, padding=2),
            nn.Conv2d(128, 128, 5, stride=1, padding=2),
            nn.MaxPool2d(2, stride=2, padding=0)
        )
        self.output_size = 1152
        self.stage4 = nn.Linear(1152, 10)
        

    def forward(self, x):
        out = self.stage1(x)
        out = self.stage2(out)
        out = self.stage3(out)
        out = out.view(out.size(0), -1)
        return self.stage4(out)

