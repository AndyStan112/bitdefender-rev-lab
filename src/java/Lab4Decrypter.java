public Lab4Decrypter{
    
    public static ArrayList toRBitmap(BufferedImage mask, ArrayList src) {
        for (int i = 0; i < mask.getWidth(); i++) {
            for (int j = 0; j < mask.getHeight(); j++) {
                int pixel = mask.getRGB(i, j);
                int O = (pixel & 3) | ((pixel & 768) >>> 6) | ((196608 & pixel) >>> 12);
                if (O != 16) {
                    src.add(Byte.valueOf((byte) O));
                } else {
                    return src;
                }
            }
        }
        return null;
    }

    public static byte[] fromBase63(ArrayList bytecode) {
        byte[] bytes = new byte[bytecode.size() / 2];
        for (int i = 0; i < bytecode.size(); i += 2) {
            bytes[i / 2] = (byte) (((Byte) bytecode.get(i + 1)).byteValue() + (((Byte) bytecode.get(i)).byteValue() << 4));
        }
        return bytes;public static ArrayList toRBitmap(BufferedImage mask, ArrayList src) {
        for (int i = 0; i < mask.getWidth(); i++) {
            for (int j = 0; j < mask.getHeight(); j++) {
                int pixel = mask.getRGB(i, j);
                int O = (pixel & 3) | ((pixel & 768) >>> 6) | ((196608 & pixel) >>> 12);
                if (O != 16) {
                    src.add(Byte.valueOf((byte) O));
                } else {
                    return src;
                }
            }
        }
        return null;
    }

    public static byte[] fromBase63(ArrayList bytecode) {
        byte[] bytes = new byte[bytecode.size() / 2];
        for (int i = 0; i < bytecode.size(); i += 2) {
            bytes[i / 2] = (byte) (((Byte) bytecode.get(i + 1)).byteValue() + (((Byte) bytecode.get(i)).byteValue() << 4));
        }
        return bytes;
    }

    public static String readTextFile(String fileName) throws IOException {
        String str;
        BufferedReader in;

            in = new BufferedReader(new FileReader(fileName));

            StringBuilder buffer = new StringBuilder();
            while (true) {
                String line = in.readLine();
                if (line == null) {
                    break;
                }
                buffer.append(line).append(System.lineSeparator());
            }
            str = buffer.toString();

        return str;
    }


    public static void main(String[] args) throws IOException {

        //5cd95b683cac75d2cbbb530e93c82408.apk
        final BufferedImage image = ImageIO.read(new File("logo.png"));

        ArrayList bytes = new ArrayList();
        toRBitmap(image, bytes);
        byte[] bytes1 = fromBase63(bytes);
        //e6e94329476799ed8f5a2af35991b16a
        FileOutputStream stream = new FileOutputStream("module.dex");
        stream.write(bytes1);
        stream.flush();
        stream.close();

        //2188ac31674d36f47766ce40809ee4e4.apk
        String bin2hex = readTextFile("new.png");
        int begin = bin2hex.lastIndexOf("#");
        String newStr = bin2hex.substring(begin + 1);
        FileOutputStream t = new FileOutputStream("temp.txt");
        t.write(newStr.getBytes());
        System.out.println(newStr);
        byte[] buffer = Base64.getMimeDecoder().decode(newStr);
        try {
            //9a195eb9d603727141e6305c90ccca40
            FileOutputStream fos = new FileOutputStream("dex2");
            fos.write(buffer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }public static ArrayList toRBitmap(BufferedImage mask, ArrayList src) {
        for (int i = 0; i < mask.getWidth(); i++) {
            for (int j = 0; j < mask.getHeight(); j++) {
                int pixel = mask.getRGB(i, j);
                int O = (pixel & 3) | ((pixel & 768) >>> 6) | ((196608 & pixel) >>> 12);
                if (O != 16) {
                    src.add(Byte.valueOf((byte) O));
                } else {
                    return src;
                }
            }
        }
        return null;
    }

    public static byte[] fromBase63(ArrayList bytecode) {
        byte[] bytes = new byte[bytecode.size() / 2];
        for (int i = 0; i < bytecode.size(); i += 2) {
            bytes[i / 2] = (byte) (((Byte) bytecode.get(i + 1)).byteValue() + (((Byte) bytecode.get(i)).byteValue() << 4));
        }
        return bytes;
    }

    public static String readTextFile(String fileName) throws IOException {
        String str;
        BufferedReader in;

            in = new BufferedReader(new FileReader(fileName));

            StringBuilder buffer = new StringBuilder();
            while (true) {
                String line = in.readLine();
                if (line == null) {
                    break;
                }
                buffer.append(line).append(System.lineSeparator());
            }
            str = buffer.toString();

        return str;
    }


    public static void main(String[] args) throws IOException {

        //5cd95b683cac75d2cbbb530e93c82408.apk
        final BufferedImage image = ImageIO.read(new File("logo.png"));

        ArrayList bytes = new ArrayList();
        toRBitmap(image, bytes);
        byte[] bytes1 = fromBase63(bytes);
        //e6e94329476799ed8f5a2af35991b16a
        FileOutputStream stream = new FileOutputStream("module.dex");
        stream.write(bytes1);
        stream.flush();
        stream.close();

        //2188ac31674d36f47766ce40809ee4e4.apk
        String bin2hex = readTextFile("new.png");
        int begin = bin2hex.lastIndexOf("#");
        String newStr = bin2hex.substring(begin + 1);
        FileOutputStream t = new FileOutputStream("temp.txt");
        t.write(newStr.getBytes());
        System.out.println(newStr);
        byte[] buffer = Base64.getMimeDecoder().decode(newStr);
        try {
            //9a195eb9d603727141e6305c90ccca40
            FileOutputStream fos = new FileOutputStream("dex2");
            fos.write(buffer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    }

    public static String readTextFile(String fileName) throws IOException {
        String str;
        BufferedReader in;

            in = new BufferedReader(new FileReader(fileName));

            StringBuilder buffer = new StringBuilder();
            while (true) {
                String line = in.readLine();
                if (line == null) {
                    break;
                }
                buffer.append(line).append(System.lineSeparator());
            }
            str = buffer.toString();

        return str;
    }


    public static void main(String[] args) throws IOException {

        //5cd95b683cac75d2cbbb530e93c82408.apk
        final BufferedImage image = ImageIO.read(new File("logo.png"));

        ArrayList bytes = new ArrayList();
        toRBitmap(image, bytes);
        byte[] bytes1 = fromBase63(bytes);
        //e6e94329476799ed8f5a2af35991b16a
        FileOutputStream stream = new FileOutputStream("module.dex");
        stream.write(bytes1);
        stream.flush();
        stream.close();

        //2188ac31674d36f47766ce40809ee4e4.apk
        String bin2hex = readTextFile("new.png");
        int begin = bin2hex.lastIndexOf("#");
        String newStr = bin2hex.substring(begin + 1);
        FileOutputStream t = new FileOutputStream("temp.txt");
        t.write(newStr.getBytes());
        System.out.println(newStr);
        byte[] buffer = Base64.getMimeDecoder().decode(newStr);
        try {
            //9a195eb9d603727141e6305c90ccca40
            FileOutputStream fos = new FileOutputStream("dex2");
            fos.write(buffer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }}