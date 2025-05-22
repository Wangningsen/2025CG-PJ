import cadquery as cq
w0=cq.Workplane('YZ',origin=(-79,0,0))
r=w0.sketch().arc((-24,-38),(-23,0),(7,24)).segment((7,87)).arc((-98,47),(-24,-38)).assemble().finalize().extrude(124).union(w0.sketch().segment((-82,-61),(-80,-99)).segment((-5,-94)).segment((-6,-81)).segment((100,-81)).segment((100,-17)).segment((-37,-17)).segment((-37,-58)).close().assemble().finalize().extrude(158))