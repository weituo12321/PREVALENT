import pickle
import matplotlib.pyplot as plt
import matplotlib as m
import numpy as np
import matplotlib.ticker as ticker
import numpy as np
from matplotlib.pylab import setp
from matplotlib import gridspec

# 5671
sentences = ["walk to the left of the clock and down the hallway to the right . Turn right before the shelf and stop in the doorway of the bedroom . ",
"Go to the left of the wooden counter with the large mirror behind it . Take the corridor on the right . Turn right at the bookcase . Walk to the end of this hall and stop just inside the bedroom . ",
"Exit the room going straight . Turn right go down the hallway until you get to a black bookcase . Turn right and continue going down the hallway until you get to a bedroom . Wait at the entrance . "]

# # 6712
# sentences = ["Go up the stairs . Turn left and stop inside the exercise room .",
# "Go up the stairs and turn left through the glass doors until you reach the first exercise machine . ",
# "Continue up the stairs and wait inside the gym . "]

# 3263
# sentences = ["Move ahead in between bar and table to the chair. ",
#       "Turn to your left and walk past the sports items on display. Stop when you reach the wood bench in the middle of the room. You should be facing the TV. ",
#       "Walk across the room, keeping the railing on your left.  Once you reach the sitting area, stop in front of the abacus on the right side of the first stuffed chair. "]

with open("alpha5671.pkl",'rb') as alpha_f:
# with open("alpha6712.pkl",'rb') as alpha_f:
# with open("alpha3263.pkl",'rb') as alpha_f:
    all_alpha = pickle.load(alpha_f)

att_reshape = [[] for _ in range(len(all_alpha[0]))] + []

for t, alpha_t in enumerate(all_alpha):
    for i, alpha_t_si in enumerate(alpha_t):
        att_reshape[i].append(alpha_t_si.squeeze(0).cpu().data.numpy())

for i, att_si in enumerate(att_reshape):
    att_reshape[i] = np.array(att_si)[:,::-1]

cdict = {
  'blue'  :  ( (0.0, 1.0, 1.0), (0.5, 0.5, .5), (1., .8, .8)),
  'green':  ( (0.0, 1.0, 1.0), (0.1, 0.02, .02), (0.5, 0.1, .1), (1., 0.0, 0.0)),
  'red' :  ( (0.0, 1.0, 1.0), (0.1, 0.02, .02), (0.5, 0.1, .1), (1., 0.0, 0.0))
}

cdict = {
  'blue'  :  ( (0.0, 1.0, 1.0), (0.5, 0.5, .5), (1., .8, .8)),
  'green':  ( (0.0, 1.0, 1.0), (0.1, 0.3, .3), (0.5, 0.08, .08), (1., 0.0, 0.0)),
  'red' :  ( (0.0, 1.0, 1.0), (0.1, 0.3, .3), (0.5, 0.08, .08), (1., 0.0, 0.0))
}
cm = m.colors.LinearSegmentedColormap('my_colormap', cdict, 1024)

def showAttention(input_sentence, output_words, attentions,i):
    # Set up figure with colorbar
    ax = plt.subplot(gs[i])
    mesh = ax.matshow(attentions.T, cmap = cm)#, cmap='bone'), origin="Top"
    ax.set_anchor('S')
    # cbar = fig.colorbar(mesh,ax=ax)
    # cbar.ax.tick_params(labelsize=fontsize)
    # cbar.set_ticks(np.arange(0, 1.0, 0.4))
    # cbar.set_ticklabels(['low', 'medium', 'high'])

    # plt.subplots_adjust(top=0)
    ## Set up axes
    #setp(ax.get_xticklabels(), visible=False)
    ax.set_xticklabels([''] + output_words,fontsize=fontsize)
    ax.set_yticklabels([''] + ['<BOS>'] + input_sentence.split(' '),fontsize=fontsize)
    ax.set_aspect(aspect='auto', adjustable='box')
    ax.set_xlabel("Steps",fontsize=fontsize)
    ax.xaxis.set_label_position('top')
    # Show label at every tick
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    plt.tight_layout(w_pad=10)

fig = plt.figure(figsize=(22,20))
gs = gridspec.GridSpec(1, 3)#, width_ratios=[])
fontsize=28
for i, att_si in enumerate(att_reshape):
    showAttention(sentences[i], [str(i+1) for i in range(7)], att_si,i)

plt.savefig("attention_heatmap.png")
plt.show()
plt.close("all")