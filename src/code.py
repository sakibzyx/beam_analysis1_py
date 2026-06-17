import planesections as ps
import matplotlib.pyplot as plt


# Length of the beam
L = 25

beam = ps.newEulerBeam(L)

# beam support onditions
pinned = [1,1,0]
beam.setFixity(0, pinned)
beam.setFixity(.8*L, pinned)

# Loading Diagram

Pz = -1000

beam.addLabel(0, label = 'A')
beam.addLabel(10, label = 'E')
beam.addLabel(20, label = 'B')

beam.addVerticalLoad(15, 2*Pz, label = 'D')
beam.addVerticalLoad(25, 3*Pz, label = 'C')

beam.addDistLoadVertical(0, L*0.4, 5*Pz)

# visualizing the beam
ps.plotBeamDiagram(beam)
plt.title("Loading Diagram")
#plt.savefig("output/beam_diagram.png", dpi=300)

# instantiate the analysis object
analysis = ps.PyNiteAnalyzer2D(beam)
# Run the analysis
analysis.runAnalysis()



# Plot the ShearForce and Bending Moment Diagram
ps.plotShear(beam, scale=0.0002, yunit='kN')
plt.title("SFD")
#plt.savefig("output/sfd.png", dpi=300)

ps.plotMoment(beam, scale=0.0002, yunit='kNm')
plt.title("BMD")
#plt.savefig("output/bmd.png", dpi=300)


plt.show()

git config --global user.name "SakibZYX"
cd D:\beam_analysis1_py

git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"

git remote add origin 