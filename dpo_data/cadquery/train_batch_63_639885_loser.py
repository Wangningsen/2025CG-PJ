import cadquery as cq
w0=cq.Workplane('YZ',origin=(-31,0,0))
r=w0.sketch().push([(-4,-7)]).circle(37).push([(79,-92)]).circle(8).finalize().extrude(22).union(w0.sketch().segment((-87,38),(-76,38)).segment((-76,24)).segment((-58,24)).segment((-58,86)).segment((-4,86)).segment((-4,96)).segment((-66,96)).segment((-66,100)).segment((-87,100)).close().assemble().finalize().extrude(61))