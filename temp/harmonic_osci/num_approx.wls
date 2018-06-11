#!/usr/bin/env wolframscript
(* ::Package:: *)

(* ::Chapter:: *)
(*1 -Dimensional Quantum Harmonic Oscillator*)

(*Exact Expression*)
Exact=N[Exp[-1/2 4](1/Pi)^(1/2) (Exp[-x^2/2])^2]/.x->{0,.25,.5,.75,1,1.25,1.5,1.75,2};

(*Parameters*)
d=6;  (*Number of steps*)
a=4/d; (*Lattice spacing*)
x={0,.25,.5,.75,1,1.25,1.5,1.75,2};
l=2; (*Integration Interval*)

(*Numerical Approximation*)
Approx=NIntegrate[(1/(2Pi a))^(d/2) Exp[-(1/2)(1/a ((Subscript[x, 1]-x)^2+(Subscript[x, 2]-Subscript[x, 1])^2+(Subscript[x, 3]-Subscript[x, 2])^2+(Subscript[x, 4]-Subscript[x, 3])^2+(Subscript[x, 4]-Subscript[x, 5])^2+(Subscript[x, 5]-x)^2)+a(Subscript[x, 1]^2+Subscript[x, 2]^2+Subscript[x, 3]^2+Subscript[x, 4]^2+Subscript[x, 5]^2+2 x^2))],{Subscript[x, 1],-l,l},{Subscript[x, 2],-l,l},{Subscript[x, 3],-l,l},{Subscript[x, 4],-l,l},{Subscript[x, 5],-l,l},WorkingPrecision->7];

ListPlot[{Exact,Approx},Frame->True,DataRange->{0,2},PlotRange->{0,.1},PlotLegends->{"Exact Expression","Numerical Approximation"}]
