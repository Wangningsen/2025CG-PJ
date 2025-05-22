import cadquery as cq
w0=cq.Workplane('YZ',origin=(-79,0,0))
r=w0.sketch().segment((-66,-99),(-60,-100)).segment((-59,-86)).arc((-62,-93),(-66,-99)).assemble().finalize().extrude(110).union(w0.sketch().push([(29,92)]).rect(74,16).reset().face(w0.sketch().segment((37,91),(48,92)).segment((48,97)).segment((37,96)).close().assemble(),mode='s').finalize().extrude(159))