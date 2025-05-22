import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
r=w0.sketch().push([(-36,0)]).circle(64).push([(64,-20.5)]).rect(10,35).finalize().extrude(-38).union(w0.sketch().arc((46,-52),(61,-56),(75,-55)).arc((75,-52),(78,-53)).arc((86,7),(31,-3)).segment((30,-3)).segment((30,-5)).arc((25,-21),(30,-37)).segment((30,-39)).segment((46,-48)).close().assemble().finalize().extrude(4))