String.prototype.eightBitNumber = function(): boolean {
    const regex = /^(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$/
    return regex.test(this.toString());
}