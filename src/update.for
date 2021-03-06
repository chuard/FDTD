C
       SUBROUTINE UPDATE(D_HY,D_HX,D_EZ,DX,DT,NTH,N)
C
CF2PY  INTENT(IN,OUT) D_HY
CF2PY  INTENT(IN,OUT) D_HX
CF2PY  INTENT(IN,OUT) D_EZ
C
!$     USE OMP_LIB
       INTEGER N,NTH
       DIMENSION D_HY(N,N),D_HX(N,N),D_EZ(N,N) 
       DOUBLE PRECISION D_HY,D_HX,D_EZ,DT,DX,DMU0,DE0,DK_H,DK_E
C
       DMU0 = 1.25663706D-6
       DE0  = 8.854187817D-12
       DK_H=DT/DX/DMU0
       DK_E=DT/DX/DE0
C
       CALL OMP_SET_NUM_THREADS(NTH)
C
!$OMP  PARALLEL DEFAULT(SHARED) PRIVATE(I,J)
!$OMP  DO
       DO 100 J=1,N
       DO 100 I=1,N
         D_HX(I,J)=D_HX(I,J)-DK_H*(D_EZ(I,J+1)-D_EZ(I,J))
         D_HY(I,J)=D_HY(I,J)+DK_H*(D_EZ(I+1,J)-D_EZ(I,J))
  100  CONTINUE
!$OMP  END DO
C
!$OMP  DO
       DO 200 J=2,N-1
       DO 200 I=2,N-1
         D_EZ(I,J)=D_EZ(I,J)+DK_E*(D_HY(I,J)-D_HY(I-1,J)) - 
     +                       DK_E*(D_HX(I,J)-D_HX(I,J-1))
  200  CONTINUE
!$OMP  END DO
!$OMP  END PARALLEL
C
       RETURN
       END
