import cadquery as cq
w0=cq.Workplane('YZ',origin=(1,0,0))
r=w0.sketch().segment((-76,-100),(29,-100)).segment((29,-48)).arc((76,3),(29,54)).segment((29,100)).segment((18,100)).segment((18,90)).segment((-76,90)).close().assemble().push([(-24,-5)]).circle(21,mode='s').finalize().extrude(-2)