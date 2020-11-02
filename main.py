import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

single_text = gpt2.generate(sess,
              length=60,
              temperature=0.7,
              prefix="Meu amor",
              nsamples=5,
              batch_size=5,
              return_as_list=True)[0]

# print(single_text)
              