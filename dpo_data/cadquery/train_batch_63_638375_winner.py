import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,38))
w1=cq.Workplane('XY',origin=(0,0,44))
r=w0.sketch().push([(-1,27)]).circle(5).push([(41,28)]).circle(12).finalize().extrude(-82).union(w0.sketch().push([(-55,-2)]).circle(45).push([(-70,-8)]).circle(26,mode='s').push([(-1,27)]).circle(17).finalize().extrude(-6)).union(w1.sketch().segment((-15,16),(13,16)).segment((13,-12)).segment((31,-12)).arc((56,-24),(82,-12)).segment((100,-12)).segment((100,35)).segment((82,35)).arc((56,47),(31,35)).segment((13,35)).segment((13,38)).segment((-15,38)).close().assemble().finalize().extrude(-15))