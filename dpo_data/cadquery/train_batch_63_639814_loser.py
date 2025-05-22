import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
w1=cq.Workplane('XY',origin=(0,0,31))
r=w0.sketch().segment((-6,9),(24,9)).segment((24,20)).arc((32,40),(24,59)).segment((24,58)).segment((-6,58)).arc((-24,34),(-6,13)).close().assemble().push([(69,-28)]).circle(31).finalize().extrude(-36).union(w0.sketch().push([(-63,-53)]).circle(37).push([(-59,-61)]).rect(24,30,mode='s').finalize().extrude(-25)).union(w1.sketch().arc((-4,19),(20,-7),(13,27)).segment((13,19)).close().assemble().finalize().extrude(59))