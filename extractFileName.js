class FileNameExtractor{
    static extraFileName(dirtyFileName){
        const regex = /^[0-9]+_([a-zA-Z0-9_-]+\.[a-zA-Z0-9]+)\./;

        const match = dirtyFileName.match(regex)

        return match ? match[1] : null;

    }
}

