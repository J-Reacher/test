#include <stdio.h>

void lap_bang(int r, s)
{
    fillchar(u, sizeof(u), 0);
    fillchar(l, sizeof(l), 0);
    for (int s = 0; s < n; s++)
        for (int r = 0; r < c; r++)
            if (s == 1)
            {
                u[r][l] = r div m[l];
                l[r][l] = u[r][l] * v[l];
            }
}

void tinhUL(int r, s)
{
    int k, k1, max, tam_thoi;
    k1 = 0;
    max = L[r][s - 1];
    for (k = 1; k <= r div m[s]; k++)
    {
        tam_thoi = k * c[s] + l[r - k * m[s]][s - 1];
        if (tam_thoi > max)
        {
            max = tam_thoi;
            k1 = k;
        }
    }
    u[r, s] = k1;
    l[r, s] = max;
}

void tonghopKQ()
{
    int r, s, i;
    r = p;
    for (s = n; s >= 1; s--)
    {
        x[s] = u[r][s];
        r = r - x[s] * m[s];
    }
    printf("Tri gia toi uu: %d", L[p][n]);
    printf("Cac vat duoc chon:");
    for (int i = 0; i < n; i++)
        printf("Vat thu %d so luong %d", i, x[i]);
}

int main()
{
    int n = 5; // So luong do vat
    lap_bang(n);
    tonghopKQ();
    return 0;
}