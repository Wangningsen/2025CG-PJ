import cadquery as cq
w0=cq.Workplane('YZ',origin=(29,0,0))
r=w0.sketch().push([(-53,84)]).rect(84,30).push([(51,19.5)]).rect(98,29).finalize().extrude(-58).union(w0.sketch().segment((-100,-86),(-25,-99)).segment((-11,-13)).segment((-85,0)).close().assemble().finalize().extrude(-17))