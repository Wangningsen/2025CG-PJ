import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,2))
r=w0.sketch().arc((-35,5),(-27,-98),(31,-12)).arc((25,98),(-35,5)).assemble().push([(-11.5,-45.5)]).rect(17,51,mode='s').finalize().extrude(-84).union(w0.sketch().segment((-16,-67),(-7,-67)).segment((-7,-24)).segment((-16,-24)).segment((-16,-41)).arc((-14,-42),(-16,-43)).close().assemble().finalize().extrude(80))