from collections import defaultdict

class Config:
    def __init__(self):
        self.heads = {}
        self.deps = defaultdict(lambda: [])




def non_projective(conf):
    print 'non_projective keys:', str(conf.heads.keys())
    for dep1 in conf.heads.keys():
        head1 = conf.heads[dep1]
        for dep2 in conf.heads.keys():
            head2 = conf.heads[dep2]
            print 'processing head1:', str(head1), ' dep1:', str(dep1), " head2:", str(head2), " dep2:", str(dep2)
            if head1 < 0 or head2 < 0:
                continue
            if (dep1 > head2 and dep1 < dep2 and head1 < head2) or (dep1 < head2 and dep1 > dep2 and head1 < dep2):
                print 'True1:dep1,dep2,head1,head2', dep1, dep2, head1, head2
                return True

            if dep1 < head1 and head1 is not head2:
                if (head1 > head2 and head1 < dep2 and dep1 < head2) or (
                            head1 < head2 and head1 > dep2 and dep1 < dep2):
                    print 'True2:dep1,dep2,head1,head2', dep1, dep2, head1, head2
                    return True
    print 'false'
    return False

if __name__ == '__main__':
    conf = Config()
    conf.heads={0: 8, 1: 2, 2: 0, 3: 8, 4: 6, 5: 6, 6: 8, 7: 6, 8: 22, 9: 8, 10: 11, 11: 9, 12: 9, 13: 16, 14: 15, 15: 16, 16: 12, 17: 16, 18: 16, 19: 18, 20: 19, 21: 8}
    #conf.deps
    print str(conf.heads)
    #, str(conf.deps)
    print non_projective(conf)

