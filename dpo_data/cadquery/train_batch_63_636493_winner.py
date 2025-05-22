import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-80,0))
r=w0.sketch().segment((-58,-27),(-19,-27)).segment((-19,-100)).segment((56,-100)).segment((56,-27)).segment((58,-27)).segment((58,98)).segment((-58,100)).close().assemble().push([(-5,53)]).circle(24,mode='s').finalize().extrude(160)