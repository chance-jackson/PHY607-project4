import finesse
import finesse.detectors as fd
import finesse.components as fc
import finesse.analysis.actions as fac
import matplotlib.pyplot as plt 

# Initialize FINESSE plotting. This is required for using sol.plot()
finesse.configure(plotting = True)

####### Building the Cavity #######################################################

# The first step in any FINESSE simulation is the initialization of your model, the "# optical bench" upon which the simulation takes place. 
# Initialize the model below, giving it some appropriate name
# The syntax is:
# finesse.Model()



# Now, we can add some components to our model. We'll start with a source/laser.
# Add a laser to your model, with power P = 1.
# The syntax is:
# fc.Laser(name: str, P: float)



# And then some mirrors. In order to properly initialize a mirror, you must specify
# at least two of three of Reflectivity (R), Transmissivity (T), and Loss (L). These # must add up to 1, or FINESSE will throw an error.
# Add two mirrors to your model, each with R = 0.9 and T = 0.1
# The syntax is:
# fc.Mirror(name: str, R: float, T: float, L: float)

model.add(...)

# We then have to connect our components. There's actually quite a few ways to do
# this in FINESSE, but we'll use the connect command, which automatically populates
# your model with space components between your specified nodes.
# Use the connect command to link the laser to M1, and M1 to M2.
# The syntax is: 
# finesse.Model.connect(portA, portB, L: float)



# The last piece we'll add to our model are a few photodetectors (called power
# detectors in FINESSE). Add three power detectors.
# The syntax for a power detector is:
# fd.PowerDetector(name: str, node)

pd_circ = model.add(...)
pd_refl = model.add(...)
pd_tran = model.add(...)

####### Running Simulations #######################################################

# Simulations in FINESSE are done by sweeping some parameter (maybe the length of
# some cavity, or the frequency of a laser) and storing the steady-state optical
# field amplitudes at every node of the model at every step. We'll sweep over the
# "tuning" of one of our mirrors in order to observe the resonance of our optical cavity

# The first thing we'll need is the Xaxis command, which tells FINESSE which 
# parameter to sweep over. The syntax for this is very similar to the components
# above:
# model.run(fac.Xaxis(parameter, mode, start, stop, steps)
# Note, there are two options for mode 'lin' or 'log'. 
# Use this to linearly sweep over the tuning of M1 (M1.phi) from -180 to 180 degrees # over 400 steps

sol = model.run(...)

#The solution object, sol, is a dictionary-type object that stores the light field 
#amplitudes at every step of your simulation sweep. The keys of this dictionary are the names of your detectors
# Finally, we can plot the solution object using sol.plot(), do this below


# Alternatively, if you aren't a fan of the in-built FINESSE plotting, you can access the solution object as you would a dictionary:

xaxis = sol.x1 #This returns a list of your parameter values at every sim step
reflected_power = sol[...] #Remember, the keys are the names of your power detectors.

# You could then plot this with matplotlib or whatever suits your fancy. If we have time, try plotting it in matplotlib and make sure that it matches the plot
# Returned by FINESSE

