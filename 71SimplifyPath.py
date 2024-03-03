class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for directory in path.split('/'):
            if directory == '..':
                if stack:
                    stack.pop()
            elif directory and directory != '.':
                stack.append(directory)
        return '/' + '/'.join(stack)