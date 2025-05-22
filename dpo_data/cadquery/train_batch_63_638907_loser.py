import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-67))
r=w0.sketch().segment((-71,-100),(44,-100)).segment((44,-10)).segment((71,-10)).segment((71,100)).segment((-38,100)).segment((-38,25)).segment((-71,25)).close().assemble().push([(-66,-80)]).circle(5,mode='s').finalize().extrude(133)