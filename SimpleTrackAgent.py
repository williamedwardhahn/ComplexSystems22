# import os
# os.system("pip install --ignore-installed  git+https://github.com/williamedwardhahn/DeepZoo")
# Action Vector: 
# Dim0 -> 1 Foward / 2 Reverse, 
# Dim1 -> 1 Strafe Right / 2 Strafe Left, 
# Dim2 -> 1 Turn Counter / 2 Turn Clock, 
# Dim3 -> 0 Null / 1 Null
#########################################
from DeepZoo import *
import torch
import torch.nn.functional as F


def GPU(data):
    return torch.tensor(data, requires_grad=True, dtype=torch.float, device=torch.device('cuda'))

def GPU_data(data):
    return torch.tensor(data, requires_grad=False, dtype=torch.float, device=torch.device('cuda'))

env = start("Fox_Track")

w_best = 0#torch.load("weights_track.npy")
i_best = 1

N = 100
for j in range(1000):

    action = np.array([[0,0,0,0]])      

    state,reward = step(env,action)

    s = state.flatten()
    
    w = w_best + 0.01 * (torch.rand(3*N,s.shape[0]))

    for i in range(1000):
        
        y = w@(state.flatten())
        
        y = F.max_pool1d(y[None,None,:],N)[0,0,:]
                
        a = torch.argmax(y,0).numpy()
                
        action = np.array([[1,0,a,0]])      
        
        state,reward = step(env,action)
        
        # plot(state)
        # print(reward)
        # 
        if reward < 0:
        
            if i > i_best:
                i_best = i
                w_best = w
                print("New best: ",i_best)
        
            env.reset()
            break

torch.save(w_best,"weights_track")
    
    
    
    
    
    
    
    
    
    
    
    
