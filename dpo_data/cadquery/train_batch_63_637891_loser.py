import cadquery as cq
w0=cq.Workplane('YZ',origin=(11,0,0))
r=w0.sketch().segment((-7,68),(7,-36)).segment((65,-28)).segment((65,-69)).segment((100,-69)).segment((100,-7)).segment((70,-7)).segment((59,77)).close().assemble().finalize().extrude(-71).union(w0.sketch().push([(-52,-52.5)]).rect(96,51).push([(74,9)]).rect(6,104).finalize().extrude(49))