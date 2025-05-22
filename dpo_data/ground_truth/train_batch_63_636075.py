import cadquery as cq
w0=cq.Workplane('YZ',origin=(93,0,0))
r=w0.sketch().push([(-28,0)]).circle(9).push([(91,41.5)]).rect(16,37).finalize().extrude(-192).union(w0.sketch().push([(-28,0)]).circle(71).circle(60,mode='s').finalize().extrude(-125)).union(w0.sketch().push([(-28.5,0)]).rect(141,200).push([(-28,0)]).circle(14,mode='s').finalize().extrude(5))