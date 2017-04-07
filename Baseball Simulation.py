from visual import * 
from math import sin, cos 
import numpy as np 
from Tkinter import *
import Tkinter
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# root to gui display 
top = Tkinter.Tk()
top.wm_title("Baseball Simulation User Inputs")

# ------------------------------Parameters-----------------------------------
Xvar = IntVar()
Yvar = IntVar()
Zvar = IntVar()
XAvar =DoubleVar()
YAvar =DoubleVar()
ZAvar =DoubleVar()
Fvar= IntVar()

#main start function 
def StartSimulation():
	# User inputs
	velocityVector = vector(Xvar.get()*0.447,Yvar.get()*0.447,Zvar.get()*0.447) # input initial velocity of ball
	velocityVector_0=velocityVector
	angularVelocityVector = vector(XAvar.get(),YAvar.get(),ZAvar.get())
	frequency=Fvar.get()


	# Constant parameters
	dt = .0001                # time step 
	g  = 9.81                 # acceleration due to gravity in m/s^2
	m  = 0.145                # baseball mass in kg
	Cd = 0.47                 # drag coefficient Cd
	rho= 0.9846               # density of air in kg/m^3
	D  = 7.45/100.0           # baseball diameter in m
	R  = D/2                  # baseball radius in m
	A  = pi*(R**2)            # baseball cross-sectional area in m^2
	Dm = .00065               # coefficient for Magnus force 
	t  = np.linspace(0,dt,5)  # vector of times
	N  = np.vectorize(t)      # number of time steps
	angularVelocityVectorMag=frequency*2*pi
	angularVelocityVector=vector(angularVelocityVector[0]*angularVelocityVectorMag,
		angularVelocityVector[1]*angularVelocityVectorMag,
		angularVelocityVector[2]*angularVelocityVectorMag)


#----------------------------Functions----------------------------------------------


#function to compute acceleration given velocity
	def acceleration(v,Cd,rho,A,m,g,Dm,w):
		InitialVelocity= vector(v[0], v[1], v[2])
		InitialVelocityMagnitude= mag(InitialVelocity)

		Magnus= m*Dm*cross(w,v)
		ForceVector = (-0.5*Cd*rho*A*InitialVelocityMagnitude*v[0] + Magnus[0], 
			-0.5*Cd*rho*A*InitialVelocityMagnitude*v[1] + Magnus[1], 
			-0.5*Cd*rho*A*InitialVelocityMagnitude*v[2] - m*g + Magnus[2])

		accel = vector(ForceVector[0]/m,ForceVector[1]/m,ForceVector[2]/m)

		return accel

#----------------------------Interface-----------------------------------------------
# Set up the display window

	scenel= display(title= "Baseball Simulation",
		x=0, y=0, width=1000, height=1000, 
		range=20, backgound=color.black, 
		center= (0, 0, 0))

	#create our objects 
	ball = sphere(pos=(-13, 1, 1), radius=R*10, color=color.white, make_trail=true)
	#ball_0=	sphere(pos=(-13, 1, 1), radius=R*10, color= color.blue, make_trail=true)
	floor= box(pos=(0, 0, 0), size=(30, 0.005, 30), color=color.green)
	floor.rotate(angle=pi/2, axis=(0,1,0), origin=(0, 0, 0))
	positionVector=ball.pos
	#positionVector_0=ball_0.pos


	#---------------------------Algorithm--------s----------------------------------------------------
	#This loop puts it in to motion
	while True:

			rate(1000) # speeds it up 

			# For ball white ball
			accelerationVector= acceleration(velocityVector,Cd,rho,A,m,g,Dm,angularVelocityVector)
			MidvelocityVector=velocityVector+accelerationVector*dt/2
			MidAccelerationVector=acceleration(MidvelocityVector,Cd,rho,A,m,g,Dm,angularVelocityVector)
			positionVector=positionVector+MidvelocityVector*dt
			ball.pos=vector(positionVector[0],positionVector[2],positionVector[1])
			velocityVector=velocityVector+MidAccelerationVector*dt

			#graphV1x.extend(positionVector[0])

			# For ball blue ball (0 spin)
			#accelerationVector_0= acceleration(velocityVector,Cd,rho,A,m,g,Dm,vector(0,0,0))
			#MidvelocityVector_0=velocityVector+accelerationVector_0*dt/2
			#MidAccelerationVector_0=acceleration(MidvelocityVector_0,Cd,rho,A,m,g,Dm,vector(0,0,0))
			#positionVector_0=positionVector_0+MidvelocityVector_0*dt
			#ball_0.pos=vector(positionVector_0[0],positionVector_0[2],positionVector_0[1])
			#velocityVector_0=velocityVector_0+MidAccelerationVector_0*dt

	#print(ball.pos)
			if ball.y<0: # when ball hits the ground...
				print "ball.pos=", ball.pos, "t=" , t
				break
			
			t+=dt

#-------------------------------------------------GUi objects-----------------------------------------------------------------------
top.minsize(width=620, height=200)

L1 = Label(top, text="Enter x velocity:")
L1.pack(side= LEFT)
L1.place(x=0, y=20)
xVInput = Scale(top, orient=HORIZONTAL, from_=0, to=100, variable = Xvar)
xVInput.pack()
xVInput.place(x=100,y=0)

L2 = Label(top, text="Enter y velocity:")
L2.pack( side= LEFT)
L2.place(x=200, y=20)
yVInput = Scale(top, orient=HORIZONTAL, from_=-1, to=100, variable = Yvar)
yVInput.pack()
yVInput.place(x=300,y=0)

L3 = Label(top, text="Enter z velocity:")
L3.pack( side = LEFT)
L3.place(x=400, y=20)
zVInput = Scale(top, orient=HORIZONTAL, from_=0, to=100, variable = Zvar)
zVInput.pack()
zVInput.place(x=500,y=0)

L4 = Label(top, text="Enter x angular velocity:")
L4.pack( side = LEFT)
L4.place(x=0, y=60)
xAVInput = Scale(top, orient=HORIZONTAL, from_=-1, to=1, resolution=0.01, variable = XAvar)
xAVInput.pack()
xAVInput.place(x=100,y=40)

L5 = Label(top, text="Enter y angular velocity:")
L5.pack( side= LEFT)
L5.place(x=200, y=60)
yAVInput = Scale(top, orient=HORIZONTAL, from_=-1, to=1, resolution=0.01, variable = YAvar)
yAVInput.pack()
yAVInput.place(x=300,y=40)

L6 = Label(top, text="Enter z angular velocity:")
L6.pack( side = LEFT)
L6.place(x=400, y=60)
zAVInput = Scale(top, orient=HORIZONTAL, from_=-1, to=1, resolution=0.01, variable = ZAvar)
zAVInput.pack()
zAVInput.place(x=500,y=40)

L7 = Label(top, text="Enter frequency:")
L7.pack( side = LEFT)
L7.place(x=0, y=100)
fInput = Scale(top, orient=HORIZONTAL, from_=0, to=100, resolution=5,variable = Fvar)
fInput.pack()
fInput.place(x=100,y=80)


StartButton = Tkinter.Button(top, text ="Start", command = StartSimulation)
StartButton.pack()
StartButton.place(x=275,y=150)
top.mainloop()