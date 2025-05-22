import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,12))
w1=cq.Workplane('XY',origin=(0,0,-25))
r=w0.sketch().arc((-71,-18),(-92,-78),(-32,-77)).arc((-65,-50),(-71,-18)).assemble().push([(-85.5,-53.5)]).rect(17,1,mode='s').push([(59,51)]).circle(41).finalize().extrude(20).union(w0.workplane(offset=39/2).moveTo(21,4.5).box(24,5,39)).union(w1.workplane(offset=-25/2).moveTo(66,1).cylinder(25,23))