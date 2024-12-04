export function stackHeight2d(layers: number) {
    const ballDiameter = 1;
    if (layers <= 0){
        return 0;
    }
    return ballDiameter * (1 + (Math.sqrt(3) / 2) * (layers - 1));

}