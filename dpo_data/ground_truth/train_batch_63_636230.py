import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
r=w0.sketch().segment((89,64),(100,65)).arc((94,67),(89,64)).assemble().finalize().extrude(-21).union(w0.sketch().push([(-81.5,-37.5)]).rect(37,59).push([(-79.5,-18.5)]).rect(21,3,mode='s').reset().face(w0.sketch().segment((-83,-49),(-80,-53)).segment((-66,-42)).segment((-68,-39)).close().assemble(),mode='s').finalize().extrude(47))