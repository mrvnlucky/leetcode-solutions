func mergeAlternately(word1 string, word2 string) string {
    res := ""
    maxLen := len(word1)
    if len(word1) < len(word2) {
        maxLen = len(word2)
    }
    for i := 0; i < maxLen; i++ {
        if i < len(word1) {
            res += string(word1[i])
        }
        if i < len(word2) {
            res += string(word2[i])
        }
    }
    return res
}