import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-84,-28),(2,-28)).segment((2,-93)).segment((84,-93)).segment((84,-13)).segment((62,-13)).segment((62,93)).segment((-84,93)).close().assemble().push([(-11.5,32.5)]).rect(53,99,mode='s').finalize().extrude(-200)