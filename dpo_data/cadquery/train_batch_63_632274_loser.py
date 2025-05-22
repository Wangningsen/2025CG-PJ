import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,60,0))
w1=cq.Workplane('YZ',origin=(11,0,0))
r=w0.sketch().arc((-17,-26),(-40,-85),(19,-81)).segment((64,-81)).segment((64,-17)).segment((-17,-17)).close().assemble().finalize().extrude(-65).union(w0.sketch().arc((-14,-6),(-54,-88),(28,-44)).segment((32,-45)).segment((42,11)).segment((34,12)).arc((20,36),(3,13)).segment((-14,15)).close().assemble().finalize().extrude(-31)).union(w1.sketch().push([(-14.5,28.5)]).rect(91,97).push([(-15,28)]).circle(42,mode='s').finalize().extrude(89))