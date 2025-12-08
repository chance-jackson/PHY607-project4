import finesse
import finesse.detectors as fd
import finesse.components as fc
import finesse.analysis.actions as fac

finesse.configure(plotting = True)

####### Building the Cavity #######################################################

# The first step in any FINESSE simulation is the initialization of your model, the "# optical bench" upon which the simulation takes place. 
# Initialize the model below, giving it some appropriate name

model = finesse.Model()

# Now, we can add some components to our model. We'll start with a source/laser.
# Add a laser to your model, with power P = 1.

laser = model.add(fc.Laser("source", P = 1))

# And then some mirrors. In order to properly initialize a mirror, you must specify
# at least two of three of Reflectivity (R), Transmissivity (T), and Loss (L). These # must add up to 1, or FINESSE will throw an error.
# Add two mirrors to your model, each with R = 0.9 and T = 0.1

M1 = model.add(fc.Mirror("M1", R = 0.9, T = 0.1))
M2 = model.add(fc.Mirror("M2", R = 0.9, T = 0.1))

# We then have to connect our components. There's actually quite a few ways to do
# this in FINESSE, but we'll use the connect command, which automatically populates
# your model with space components between your specified nodes.
# Use the connect command to link the laser to M1, and M1 to M2.

model.connect(laser.p1, M1.p1, L = 1)
model.connect(M1.p2, M2.p1, L = 1)

# The last piece we'll add to our model are a few photodetectors (called power
# detectors in FINESSE). Add three power detectors.

pd_circ = model.add(fd.PowerDetector("pd_circ", M2.p1.o))
pd_tran = model.add(fd.PowerDetector("pd_tran", M2.p2.o))
pd_refl = model.add(fd.PowerDetector("pd_refl", M1.p1.o))


####### Running Simulations #######################################################

# Simulatiions in FINESSE 

out = model.run(fac.Xaxis(M1.phi, 'lin', -180, 180, 400))
out.plot()
