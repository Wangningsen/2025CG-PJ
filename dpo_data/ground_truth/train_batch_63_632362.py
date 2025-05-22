import cadquery as cq
w0=cq.Workplane('YZ',origin=(29,0,0))
r=w0.sketch().segment((-100,-41),(-32,-41)).segment((-32,-45)).segment((2,-45)).segment((2,86)).segment((-19,86)).segment((-37,86)).segment((-100,86)).close().assemble().reset().face(w0.sketch().segment((54,-80),(87,-86)).segment((100,-24)).segment((67,-17)).close().assemble()).finalize().extrude(-58)