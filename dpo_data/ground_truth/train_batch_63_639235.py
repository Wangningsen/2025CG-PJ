import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,19,0))
r=w0.sketch().segment((-100,-48),(-88,-53)).segment((-73,-13)).segment((-55,-13)).segment((-55,13)).segment((-63,13)).segment((-49,48)).segment((-62,53)).segment((-77,13)).segment((-95,13)).segment((-95,-13)).segment((-87,-13)).close().assemble().push([(70,-12)]).circle(30).finalize().extrude(-39)