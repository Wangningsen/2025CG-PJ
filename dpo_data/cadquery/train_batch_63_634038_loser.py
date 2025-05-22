import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-23))
r=w0.sketch().push([(-82,-3.5)]).rect(36,93).push([(75,25)]).circle(25).reset().face(w0.sketch().segment((56,19),(65,12)).segment((94,31)).segment((85,40)).close().assemble(),mode='s').finalize().extrude(46)