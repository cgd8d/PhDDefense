import matplotlib.pyplot

Levels = [
('Sn', 50, -56.2990, 'beta'),
('Sb', 51, -64.5250, 'beta'),
('Te', 52, -74.4790, 'beta'),
('I', 53, -79.5721, 'beta'),
('Xe', 54, -86.4291, 'betabeta'),
('Cs', 55, -86.3390, 'beta'),
('Ba', 56, -88.8872, None),
('La', 57, -86.0369, 'ec'),
('Ce', 58, -86.4736, 'ecec'),
('Pr', 59, -81.3289, 'ec'),
('Nd', 60, -79.1992, 'ec'),
('Pm', 61, -71.1979, 'ec'),
('Sm', 62, -66.8108, 'ec'),
('Eu', 63, -56.1040, 'ec'),
('Gd', 64, -48.9220, 'ec'),
('Tb', 65, -35.8900, 'ec')
]

def GetEntryForAtom(atom):
    for i in range(len(Levels)):
        if Levels[i][0] == atom: return i
def GetEntryForZ(z):
    for i in range(len(Levels)):
        if Levels[i][1] == z: return i

UpperLimit = -82

vals = []

for level in Levels:
    if level[2] > UpperLimit: continue
    if level[1] > 56: continue
    vals.append([float(level[1]), float(level[1])+1])
    vals.append([level[2], level[2]])

vals_tuple = tuple(vals)

matplotlib.pyplot.plot(*vals_tuple, color='black', lw=3)

for level in Levels:
    if level[2] > UpperLimit: continue
    if level[1] > 56: continue
    if level[0] == 'Ba':
        vertical_diffpos = 0.1
    else:
        vertical_diffpos = -0.2
    matplotlib.pyplot.annotate(r'$^{136}$' + level[0],
                               (float(level[1]) + 0.5, level[2] + vertical_diffpos),
                               ha = "center")

    if level[3] == 'beta':
        entryOfDaughter = GetEntryForZ(level[1]+1)
        matplotlib.pyplot.annotate(u'\u03B2',
                                   (float(level[1]) + 1, level[2]),
                                   xytext = (float(level[1] + 1 + Levels[entryOfDaughter][1])/2,
                                             (level[2] + Levels[entryOfDaughter][2])/2),
                                   arrowprops = dict(arrowstyle="<-"),
                                   ha = "center")

    if level[3] == 'betabeta':
        entryOfDaughter = GetEntryForZ(level[1]+2)
        matplotlib.pyplot.annotate(u'\u03B2\u03B2',
                                   (float(level[1]) + 1, level[2]),
                                   xytext = (float(level[1] + 1 + Levels[entryOfDaughter][1])/2,
                                             (level[2] + Levels[entryOfDaughter][2])/2),
                                   arrowprops = dict(arrowstyle="<-"),
                                   ha = "center")

    if level[3] == 'ec':
        entryOfDaughter = GetEntryForZ(level[1]-1)
        matplotlib.pyplot.annotate(u'\u03B5',
                                   (float(level[1]), level[2]),
                                   xytext = (float(level[1] + Levels[entryOfDaughter][1] + 1)/2,
                                             (level[2] + Levels[entryOfDaughter][2])/2),
                                   arrowprops = dict(arrowstyle="<-"),
                                   ha = "center")

    if level[3] == 'ecec':
        entryOfDaughter = GetEntryForZ(level[1]-2)
        matplotlib.pyplot.annotate(u'\u03B5\u03B5',
                                   (float(level[1]), level[2]),
                                   xytext = (float(level[1] + Levels[entryOfDaughter][1] + 1)/2,
                                             (level[2] + Levels[entryOfDaughter][2])/2),
                                   arrowprops = dict(arrowstyle="<-"),
                                   ha = "center")

matplotlib.pyplot.xlabel('Z (# Protons)')
matplotlib.pyplot.ylabel(r'$\Delta E\,$ (MeV)')
matplotlib.pyplot.gcf().set_size_inches(3.5, 5) # Try to see the Xe-Cs energy difference better.
matplotlib.pyplot.gca().set_xticks([54,55,56])
import matplotlib.ticker
matplotlib.pyplot.gca().xaxis.set_major_formatter(matplotlib.ticker.NullFormatter())
matplotlib.pyplot.gca().xaxis.set_minor_locator(matplotlib.ticker.FixedLocator([54.5,55.5,56.5]))
matplotlib.pyplot.gca().xaxis.set_minor_formatter(matplotlib.ticker.FixedFormatter(['54', '55', '56']))
matplotlib.pyplot.gca().tick_params(axis='x',which='minor',bottom='off')
#matplotlib.pyplot.gca().get_xaxis_text1_transform((0.5,0))
#for tick in matplotlib.pyplot.gca().get_xaxis().get_major_ticks():
#    tick.label1.set_horizontalalignment('center')
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.savefig('LevelDiagram.pdf')




