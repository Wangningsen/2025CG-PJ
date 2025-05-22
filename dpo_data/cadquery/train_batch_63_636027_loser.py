import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-17))
w1=cq.Workplane('YZ',origin=(-36,0,0))
r=w0.sketch().push([(48,-58)]).circle(42).push([(48.5,-58.5)]).rect(61,15,mode='s').finalize().extrude(-17).union(w0.sketch().segment((-86,-2),(-49,-2)).segment((-71,-32)).segment((-41,-53)).segment((-6,-3)).segment((-36,18)).segment((-45,5)).segment((-86,5)).close().assemble().push([(-38.5,-17.5)]).rect(29,15,mode='s').finalize().extrude(41)).union(w1.workplane(offset=-54/2).moveTo(68,30).box(64,8,54))