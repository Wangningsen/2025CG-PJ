import cadquery as cq
w0=cq.Workplane('YZ',origin=(-55,0,0))
w1=cq.Workplane('XY',origin=(0,0,26))
r=w0.sketch().push([(-30,-36)]).rect(56,128).reset().face(w0.sketch().segment((-58,-17),(-10,-67)).segment((1,-56)).segment((-47,-8)).close().assemble(),mode='s').finalize().extrude(89).union(w1.sketch().segment((-62,-14),(-54,-14)).arc((0,-54),(54,-14)).segment((62,-14)).segment((62,17)).segment((54,17)).arc((0,58),(-54,17)).segment((-62,17)).close().assemble().push([(0,2)]).rect(58,78,mode='s').finalize().extrude(74))