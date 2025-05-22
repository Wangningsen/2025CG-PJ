import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,63,0))
r=w0.sketch().push([(-13.5,-72)]).rect(75,56).push([(-3,-79)]).circle(2,mode='s').push([(13,62)]).circle(38).finalize().extrude(-126).union(w0.sketch().segment((-47,-45),(7,-45)).segment((7,41)).segment((-47,41)).segment((-47,-21)).segment((-45,-21)).segment((-45,-23)).segment((-47,-23)).close().assemble().finalize().extrude(-13))