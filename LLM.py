def actor_loss(self, logp, old_logp, adv, mask):
    log_r = logp - old_logp
    r = torch.exp(log_r)

    loss1 = - adv * r
    loss2 = - adv * torch.clamp(r, 1 - self.clamp, 1 + self.clamp)

    loss = torch.sum(torch.max(loss1, loss2) * mask) / torch.sum(mask)

    return loss


def critic_loss(self, value, old_value, returns, mask):
    value_clamp = torch.clamp(value, 0.8 * old_value, 1.2 * old_value)
    
    loss1 = (value - returns) **2
    loss2 = (value_clamp - returns) **2

    loss = torch.sum(torch.max(loss1, loss2) * mask) / torch.sum(mask)

    return loss

    import torch
    import torch.nn.functional as F 
    
    def attentioan(Q, K, V):
        score = torch.matmul(Q, K.transpose(-2, -1)) / (K.size(-1) ** 0.5)
        wight = F.softmax(score, dim = -1)
        output = torch.matmul(wight, V)
        return output


    import torch
    import torch.nn as nn
    import torch.nn.functional as F 

    class MultiHeadAttention(nn.module):
        def 
