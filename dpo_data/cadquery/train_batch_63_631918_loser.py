import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
r=w0.sketch().push([(-42,-15)]).circle(59).push([(41,23)]).circle(51).finalize().extrude(69).union(w0.sketch().segment((-19,-26),(26,-26)).arc((41,-28),(56,-26)).segment((100,-26)).segment((100,72)).segment((56,72)).arc((41,74),(26,72)).segment((-19,72)).close().assemble().finalize().extrude(117))