import cadquery as cq
w0=cq.Workplane('YZ',origin=(-53,0,0))
r=w0.sketch().segment((-100,-85),(15,-85)).segment((15,10)).segment((100,10)).segment((100,13)).segment((65,12)).segment((65,85)).segment((-100,85)).close().assemble().push([(-90,0)]).rect(12,12,mode='s').finalize().extrude(107)