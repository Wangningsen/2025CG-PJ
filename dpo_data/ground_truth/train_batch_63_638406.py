import cadquery as cq
w0=cq.Workplane('YZ',origin=(21,0,0))
r=w0.workplane(offset=-42/2).moveTo(-7,-29).cylinder(42,71).union(w0.sketch().segment((56,-48),(59,-48)).segment((59,4)).arc((77,22),(59,39)).segment((59,100)).segment((56,100)).segment((56,39)).arc((42,22),(56,5)).close().assemble().finalize().extrude(-21))