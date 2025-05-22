import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
r=w0.sketch().push([(16,-12)]).circle(24).push([(-3,-5)]).circle(2,mode='s').finalize().extrude(-39).union(w0.sketch().arc((-45,46),(-87,-30),(-1,-22)).arc((22,-23),(38,-8)).segment((9,-8)).segment((9,30)).segment((41,30)).arc((4,100),(-45,46)).assemble().push([(85.5,-62)]).rect(21,76).finalize().extrude(-5))